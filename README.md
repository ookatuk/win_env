# win_env 1.1.3

This is a library that allows you to display and set Windows system environment variables and user environment variables.

## Description

This module uses the winreg module to edit the location of environment variables.

## Usage

### env_type

#### ```win_env.user```

Specifies the user environment variables.

#### ```win_env.systems```

Specifies the system environment variables.

#### ```win_env.custom```

Think of it as a carry-over variable.
It's stored in a Registry so it can be easily seen from outside.

Registry location: ```HKEY_CURRENT_USER\Software\python-lib\3.12\win_env\custom_env```

#### ```win_env.volatile``` (beta)

Specifies a volatile environment variable.
There seems to be a bug in Windows so it may not work properly.

### write_mode

#### 1

  Write it in REG_SZ format, not in list format, which indicates that you haven't specified a location.

#### 2

  Specify 2 to specify location or list format, written as REG_EXPAND_SZ.

### Multiple Placement Commands

#### ```win_env.open(env_type)```

You can use either a variable or with.

Available commands

##### ```list(only=None)```

Same as list command

##### ```get(key)```

Same as get command

##### ```set(key, value, write_mode=1)```

Same as set command

##### ```dels(key)```

Same as dels command

##### ```add(key, value, write_mode=1)```

Same as add command

### Single command

#### ```win_env.list(env_type, only=None)```
  Lists the contents of the environment variables.

Only args: False will return a list of just the values, True will return just the keys, None will return both.

#### only

False returns a list of only the values. True returns only the keys.
defolt = None

#### ```win_env.get(env_type, key)```

Displays the contents of the environment variable named key.

#### ```win_env.set(env_type, key, value, write_mode)```

Write the environment variables.

Note: Run as administrator to write system environment variables.

#### ```win_env.all_list()```

Returns all environment variables as a dictionary+list.

#### ```win_env.dels(env_type, key)```

Removes an environment variable. Returns Env NotFoundError of the environment variable does not exist.

Note: Admin privileges are required for system environment variables.

#### ```win_env.add(env_type, key, value, write_mode)```


Adds the environment variable if it doesn't exist, raises an EnvError if it does exist.

## How to install

```pip install git+https://github.com/ookatuk/win_env.git```

or

```pip install win_all_env```

in the command prompt.
