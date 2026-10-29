#!/usr/bin/env python3
"""PreToolUse-хук: запрещает Claude разрушающие SQL-команды (TRUNCATE, DROP, DELETE FROM, ALTER … DROP).
Рабочая база lingvaden.ru — продакшен с данными владельца. Удаление — только через админку или кабинет."""
import json, re, sys
d = json.load(sys.stdin)
cmd = (d.get("tool_input") or {}).get("command", "") or ""
if re.search(r"(?i)\b(truncate\b|drop\s+(table|database|schema)\b|delete\s+from\b|alter\s+table\b[^;]*\bdrop\b)", cmd):
    print("Заблокировано: разрушающий SQL на рабочей базе запрещён (правило владельца, CLAUDE.md). "
          "Удаляйте данные только через админку/кабинет и только с явного согласия владельца.", file=sys.stderr)
    sys.exit(2)
