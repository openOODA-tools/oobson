# oobson: Sovereign BSON SERIALIZER

<div align="center">

```
================================================================================
                                oobson
               Sovereign openOODA BSON SERIALIZER
================================================================================
```

**Sovereign BSON SERIALIZER**  
*Binary JSON encoder and decoder with bson-to-json streaming converters.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oobson/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oobson-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oobson/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oobson/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oobson-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oobson/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oobson [options] [INPUT]

Binary JSON encoder and decoder with bson-to-json streaming converters.

Options:
  -h, --help           display this help and exit
  -v, --version        output version information and exit
  -i, --input <FILE>   input file path or hex string
  -t, --to <FORMAT>    target format: json, bson, or hex [default: json]
      --inspect        inspect BSON header, element types, and offsets
      --json           output formatted as structured JSON
      --color <WHEN>   colorize output: auto, always, never [default: auto]
      --theme <NAME>   override active oote palette
      --mcp            run as Model Context Protocol stdio server
```

---

## 3. Theming Integration (`oote`)

`oobson` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oobson` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

* `bson_decode`: Decode BSON hex byte string into structured JSON.
* `bson_encode`: Encode simple JSON object (strings and int32 fields) into BSON hex bytes.
* `bson_inspect`: Inspect BSON hex byte structure, headers, elements, types, and byte offsets.
* `bson_stats`: Calculate statistics and element counts for BSON payload.

```bash
oobson --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&FsReadCap, &StreamCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
