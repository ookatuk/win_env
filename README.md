# win_env 1.0.1

This is a library that allows you to display and set Windows system environment variables and user environment variables.

## Description

This module uses the winreg module to edit the location of environment variables.

## Usage

### env_type

#### ```win_env.user```

Specifies the user environment variables.

#### ```win_env.systems```

Specifies the system environment variables.

#### ```win_env.volatile``` (beta)

Specifies a volatile environment variable.
There seems to be a bug in Windows so it may not work properly.

### write_mode

#### 1

  Write it in REG_SZ format, not in list format, which indicates that you haven't specified a location.

#### 2

  Specify 2 to specify location or list format, written as REG_EXPAND_SZ.

### command

#### ```win_env.lists(env_type)```
  Lists the contents of the environment variables.

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


Run

```pip install git+https://github.com/akino11/win_env.git```

in the command prompt.
