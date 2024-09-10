# win_env

This is a library that allows you to display and set Windows system environment variables and user environment variables.

## Description

This module uses the winreg module to edit the location of environment variables.

## Usage

### env_type

#### user

Specifies the user environment variables.

#### system

Specifies the system environment variables.

### volatile (beta)

Specifies a volatile environment variable.
There seems to be a bug in Windows so it may not work properly.

### write_mode

#### 1

  Write it in REG_SZ format, not in list format, which indicates that you haven't specified a location.

#### 2

  Specify 2 to specify location or list format, written as REG_EXPAND_SZ.

### command

#### win_env.env(env_type, "list")
  Lists the contents of the environment variables.

#### win_env.env(env_type, "get" key)

Displays the contents of the environment variable named key.

#### win_env(env_type, "set", key, value, write_mode)

Writes an environment variable named key as value.
Note: Please run as administrator.

## Install

pip install git+https://github.com/akino11/win_env.git
