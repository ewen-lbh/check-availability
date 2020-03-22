from typing import *
import pastel

class Logger:
  def __init__(self, level:int=1):
    self.level = level
    self.debug = self._make_log_function(
      level=4,
      style_normal='options=dark',
      style_value_primary='options=dark;fg=cyan',
      style_value_secondary='options=dark;fg=blue'
    )
    self.info = self._make_log_function(
      level=3,
      style_normal='fg=default',
      style_value_primary='fg=cyan',
      style_value_secondary='fg=blue'
    )
    self.warn = self._make_log_function(
      level=2,
      style_normal='fg=yellow',
      style_value_primary='fg=default',
      style_value_secondary='options=bold'
    )
    self.error = self._make_log_function(
      level=1,
      style_normal='fg=red',
      style_value_primary='fg=default',
      style_value_secondary='options=bold'
    )
    self.success = self._make_log_function(
      level=3,
      style_normal='fg=green',
      style_value_primary='fg=default',
      style_value_secondary='options=bold'
    )

  def _make_log_function(self, level, style_normal, style_value_primary, style_value_secondary):
    def _function(msg: str, data1=None, data2=None):
      msg = msg.format(
        f'<{style_value_primary}>{data1}</{style_value_primary}>' if data1 is not None else '',
        f'<{style_value_secondary}>{data2}</{style_value_secondary}>' if data2 is not None else ''
      )
      if self.level >= level:
        print(pastel.colorize(f'<{style_normal}>{msg}</{style_normal}>'))
    return _function
