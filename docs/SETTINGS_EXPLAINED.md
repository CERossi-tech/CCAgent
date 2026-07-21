# Settings spiegati

```json
{
  "permissions": {
    "allow": [
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Read",
      "Grep",
      "Glob"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(git push:*)",
      "Read(.env)",
      "Read(**/id_rsa)"
    ]
  },
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "./hooks/sessionstart_context.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python ./hooks/pretool_block_dangerous_bash.py"
          },
          {
            "type": "command",
            "command": "python ./hooks/audit_log.py"
          }
        ]
      },
      {
        "matcher": "Read|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python ./hooks/pretool_secret_guard.py"
          },
          {
            "type": "command",
            "command": "python ./hooks/pretool_no_binary_edit.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "./hooks/posttool_format_changed_files.sh"
          },
          {
            "type": "command",
            "command": "./hooks/posttool_diff_summary.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "./hooks/stop_verify_tests.sh"
          }
        ]
      }
    ]
  }
}
```

La allowlist concede solo lettura, grep, glob e comandi Git non distruttivi. La denylist blocca push, rm ricorsivo e file segreti. Gli hook dimostrano guardrail prima/dopo gli strumenti.
