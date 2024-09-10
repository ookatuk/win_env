import winreg

class EnvNotFundError(FileNotFoundError):
    def __init__(self, *args):
        print("".join(args))


def env(env_type, mode, key=None, value=None, writemode=1):
    """概要

    システム環境変数かユーザー環境変数を取得・設定します。
    :writemode: 1か2で指定してください。1は単純な文字列などに使用し、場所や複数個の場合は2を指定してください。
    :env_type: ユーザー環境変数(user)かシステム環境変数(system)か揮発性環境変数(volatile)を"str"型で指定します。
    :mode: list(一覧表示), get(値取得), set(設定)から選んでね
    :key: 引数(mode)がgetかsetの場合に使用。キーを指定してください。
    :value: 引数(mode)がsetの場合に使用。値を指定してください。
    :return: 引数(mode)がlistなら環境変数をリストにして返して、getはそれに対応する値、setはありません。
    :rtype: list or str
    :raises EnvNotFoundError: FileNotFoundError
    """
    if env_type == "system":
        keys = [winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"]
    elif env_type == "user":
        keys = [winreg.HKEY_CURRENT_USER, r"Environment"]
    elif env_type == "volatile":
        keys = [winreg.HKEY_CURRENT_USER, r"Volatile Environment"]
    else:
        raise TypeError(f"{env_type}はタイプとして存在しません。")
    with winreg.OpenKey(
        keys[0],
            keys[1]
            ) as wr:
        if mode == "list":
            values = []
            subkey, valu, time = winreg.QueryInfoKey(wr)
            for i in range(valu):
                if winreg.EnumValue(wr, i)[2] not in [1, 2]:
                    continue
                values.append(winreg.EnumValue(wr, i)[0])
            return values
        elif mode == "get":
            values = ""
            lists = env(env_type, "list")
            if key not in lists:
                raise EnvNotFundError("")
            loop = 0
            for i in lists:
                if i == key:
                    break
                loop += 1
            return winreg.EnumValue(wr, loop)[1]
        elif mode == "set":
            with winreg.CreateKeyEx(
                keys[0],
                    keys[1]
                    ) as wrr:
                if writemode == 1:
                    winreg.SetValueEx(wrr, key, 0, winreg.REG_SZ, value)
                elif writemode == 2:
                    winreg.SetValueEx(wrr, key, 0, winreg.REG_EXPAND_SZ,
                                      value)
                else:
                    raise TypeError(f"type {writemode} は存在しません。")
