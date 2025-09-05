import sys
import click


def get_version() -> str:
    """
    获取包版本：优先从包内 __version__ 读取，兜底为 0.1.0
    """
    try:
        from . import __version__  # 若 __init__.py 定义了 __version__
        return __version__
    except Exception:
        return "0.1.0"


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(version=get_version(), prog_name="chat-with-notion")
def cli() -> None:
    """
    chat-with-notion 命令行工具

    使用方式：
      chat-with-notion [命令] [选项]

    查看帮助：
      chat-with-notion --help
      chat-with-notion <命令> --help
    """
    # group 的入口，一般不需要返回值
    pass


@cli.command("version")
def version_cmd() -> None:
    """
    显示当前版本号
    """
    click.echo(f"chat-with-notion CLI (version {get_version()})")


@cli.command("hello")
@click.option("--name", "-n", default="World", help="问候对象名称")
def hello_cmd(name: str) -> None:
    """
    示例子命令：打印问候语
    """
    click.echo(f"Hello, {name}!")


def main() -> int:
    """
    兼容 [tool.poetry.scripts] 的入口函数
    """
    try:
        cli(standalone_mode=True)
        return 0
    except SystemExit as e:
        # Click 在正常退出时会抛出 SystemExit，这里捕获以返回正确的退出码
        return int(e.code) if hasattr(e, "code") and e.code is not None else 0


if __name__ == "__main__":
    sys.exit(main())
