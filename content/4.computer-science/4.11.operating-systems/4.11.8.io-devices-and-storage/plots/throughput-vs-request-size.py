"""Effective throughput of one synchronous request as a function of its size."""

import numpy as np
import matplotlib.pyplot as plt

# (name, fixed cost per request in seconds, sustained bandwidth in bytes/s)
devices = [
    ("HDD, 7200 rpm (12.2 ms, 250 MB/s)", 8e-3 + 60 / 7200 / 2, 250e6),
    ("SATA SSD (100 us, 550 MB/s)", 100e-6, 550e6),
    ("NVMe SSD (60 us, 7 GB/s)", 60e-6, 7e9),
]

size = np.logspace(np.log10(512), np.log10(1 << 30), 400)  # 512 B to 1 GiB

fig, ax = plt.subplots(figsize=(7.5, 4.6))
for k, (name, latency, bandwidth) in enumerate(devices):
    rate = size / (latency + size / bandwidth)
    ax.plot(size, rate / 1e6, color=f"C{k}", lw=2, label=name)
    ax.axhline(bandwidth / 1e6, color=f"C{k}", lw=0.8, ls=":")
    # request size at which half of the bandwidth is reached: latency * bandwidth
    half = latency * bandwidth
    ax.plot([half], [bandwidth / 2e6], "o", color=f"C{k}", ms=5)

labels = {4096: "4 KiB", 1 << 20: "1 MiB", 1 << 30: "1 GiB", 512: "512 B"}
ax.set_xscale("log", base=2)
ax.set_yscale("log")
ax.set_xticks(list(labels))
ax.set_xticklabels(list(labels.values()))
ax.set_xlabel("request size")
ax.set_ylabel("effective throughput (MB/s)")
ax.set_title("One request at a time: fixed cost vs. transfer time")
ax.grid(True, which="major", alpha=0.3)
ax.legend(loc="lower right", fontsize=9)
fig.tight_layout()
