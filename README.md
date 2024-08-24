<!-- markdownlint-disable MD033 MD036 MD041 MD045 -->
<div align="center">
  <a href="https://v2.nonebot.dev/store">
    <img src="./docs/NoneBotPlugin.svg" width="300" alt="logo">
  </a>
</div>

<div align="center">

# NoneBot-Plugin-MaiMai

_✨ NoneBot maimai DX 查分插件 ✨_

<a href="">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-lxns-maimai.svg" alt="pypi" />
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json" alt="pdm-managed">
</a>
<a href="https://github.com/nonebot/plugin-alconna">
  <img src="https://img.shields.io/badge/Alconna-resolved-2564C2" alt="alc-resolved">
</a>

<br/>

[//]: # ([![NoneBot Registry]&#40;https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin%2Fnonebot-plugin-lxns-maimai&#41;]&#40;https://registry.nonebot.dev/plugin/nonebot-plugin-lxns-maimai:nonebot_plugin_lxns_maimai&#41;)

[//]: # ([![Supported Adapters]&#40;https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin-adapters%2Fnonebot-plugin-lxns-maimai&#41;]&#40;https://registry.nonebot.dev/plugin/nonebot-plugin-lxns-maimai:nonebot_plugin_lxns_maimai&#41;)

</div>

## 📖 介绍

NoneBot maimai DX 查询插件。

## 💿 安装

以下提到的方法任选 **其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 Bot 的根目录下打开命令行, 输入以下指令即可安装

```shell
nb plugin install nonebot-plugin-lxns-maimai
```

</details>
<details>
<summary>使用包管理器安装</summary>

```shell
pip install nonebot-plugin-lxns-maimai
# or, use poetry
poetry add nonebot-plugin-lxns-maimai
# or, use pdm
pdm add nonebot-plugin-lxns-maimai
# or, use uv
uv add nonebot-plugin-lxns-maimai
```

打开 NoneBot 项目根目录下的配置文件, 在 `[plugin]` 部分追加写入

```toml
plugins = ["nonebot_plugin_lxns_maimai"]
```

</details>

## ⚙️ 配置

在项目的配置文件中添加下表中配置

|        配置项        | 必填 | 默认值 |
|:-----------------:|:--:|:---:|
| maimai__api_token | 是  |  无  |

## 🎉 使用

> [!note]
> 请检查你的 `COMMAND_START` 以及上述配置项。这里默认使用 `/`


### 绑定账号

首次绑定时请前往 [maimai DX 查分器](https://maimai.lxns.net/) 同步游戏数据，获取好友码

```shell
/m bind [friend code]
```

### Best 50

```shell
/m b50
```

## 💖 鸣谢

- [@Lxns-Network](https://github.com/Lxns-Network)：提供了超棒的 maimai DX 查分器
- [@星鹿ELEC](https://space.bilibili.com/628990513)：绘制了好康的 Best 50 查分图

## 📄 许可证

本项目使用 [MIT](./LICENSE) 许可证开源

```text
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


