#!/usr/bin/env bash
# 这是当前仓库的辅助脚本：
# 用来快速开启 / 关闭 / 查看 Git 代理配置。
set -euo pipefail

# 无论你在哪个目录执行脚本，都先切换到仓库根目录再操作。
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

# 参数说明：
# 1) mode：on / off / show（默认 on）
# 2) port：Clash 代理端口（默认 7890）
# 3) host：代理主机 IP（默认取 /etc/resolv.conf 里的 nameserver，也就是常见的 WSL 网关）
mode="${1:-on}"
port="${2:-7890}"
gateway="$(awk '/^nameserver/{print $2; exit}' /etc/resolv.conf)"
host="${3:-$gateway}"
proxy="http://${host}:${port}"

# 新手提示：根据当前动作，打印“下一步可以直接执行”的命令。
print_next_steps() {
  local state="$1"
  echo
  echo "------ 新手提示 ------"
  if [[ "$state" == "on" ]]; then
    echo "代理已开启（仅当前仓库生效）。"
    echo "下一步可执行："
    echo "  1) 检查配置：./scripts/clash-proxy.sh show"
    echo "  2) 尝试推送：git push"
    echo "  3) 关闭代理：./scripts/clash-proxy.sh off"
  elif [[ "$state" == "off" ]]; then
    echo "代理已关闭（仅当前仓库生效）。"
    echo "下一步可执行："
    echo "  1) 查看状态：./scripts/clash-proxy.sh show"
    echo "  2) 重新开启：./scripts/clash-proxy.sh on"
  else
    echo "当前是查看模式（show）。"
    echo "下一步可执行："
    echo "  1) 开启代理：./scripts/clash-proxy.sh on"
    echo "  2) 指定主机和端口开启：./scripts/clash-proxy.sh on 7890 172.30.160.1"
    echo "  3) 关闭代理：./scripts/clash-proxy.sh off"
  fi
}

case "$mode" in
  on)
    # 把代理写入“当前仓库”的 Git 本地配置（.git/config）。
    # --local 表示只影响这个仓库，不影响你其它项目。
    git config --local http.proxy "$proxy"
    git config --local https.proxy "$proxy"
    # 强制使用 HTTP/1.1，规避某些代理环境下的协议兼容问题。
    git config --local http.version HTTP/1.1
    echo "[clash-proxy] enabled: $proxy"
    print_next_steps "on"
    ;;
  off)
    # 删除当前仓库的本地代理配置。
    # 如果配置本来就不存在，"|| true" 可以避免脚本报错退出。
    git config --local --unset-all http.proxy || true
    git config --local --unset-all https.proxy || true
    echo "[clash-proxy] disabled"
    print_next_steps "off"
    ;;
  show)
    # 显示自动识别到的网络信息，以及当前仓库的代理配置值。
    echo "gateway=$gateway"
    echo "host=$host"
    git config --local --get http.proxy || echo "http.proxy=(unset)"
    git config --local --get https.proxy || echo "https.proxy=(unset)"
    print_next_steps "show"
    ;;
  *)
    # 参数不合法时，打印帮助信息。
    echo "Usage: $0 [on|off|show] [port] [host]" >&2
    exit 1
    ;;
esac
