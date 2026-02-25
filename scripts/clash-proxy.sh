#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

mode="${1:-on}"
port="${2:-7890}"
gateway="$(awk '/^nameserver/{print $2; exit}' /etc/resolv.conf)"
host="${3:-$gateway}"
proxy="http://${host}:${port}"

case "$mode" in
  on)
    git config --local http.proxy "$proxy"
    git config --local https.proxy "$proxy"
    git config --local http.version HTTP/1.1
    echo "[clash-proxy] enabled: $proxy"
    ;;
  off)
    git config --local --unset-all http.proxy || true
    git config --local --unset-all https.proxy || true
    echo "[clash-proxy] disabled"
    ;;
  show)
    echo "gateway=$gateway"
    echo "host=$host"
    git config --local --get http.proxy || echo "http.proxy=(unset)"
    git config --local --get https.proxy || echo "https.proxy=(unset)"
    ;;
  *)
    echo "Usage: $0 [on|off|show] [port] [host]" >&2
    exit 1
    ;;
esac
