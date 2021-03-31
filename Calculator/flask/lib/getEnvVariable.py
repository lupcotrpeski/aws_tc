import os


def getEnvVariable(varName):
  try:
    value = os.environ[varName]
    if value.lower() == 'true':
      return True
    elif value.lower() == 'false':
      return False
    return value
  except KeyError:
    error_msg = 'Set the {} environmental variable'.format(varName)
