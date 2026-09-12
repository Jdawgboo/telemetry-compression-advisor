# telemetry-compression-advisor

Recommend a simple lossless encoding strategy from observed telemetry values.

The advisor chooses between run-length, delta, and plain storage based on deterministic sequence traits; it does not compress data itself.

```bash
python -m unittest -v
```

MIT licensed.