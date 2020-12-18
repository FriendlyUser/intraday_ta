## Setup in Codespaces

Some of the charts available on tradingview are locked for penny stocks which is bad for me, since I mainly trade penny stocks. High risk, high reward. For ease of use across platforms, I also run these ipython notebooks in codespaces.

This project contains three parts.

1. Common plotting utilities containing yfinance and darts
2. Voila interactive dashboards for my ipython notebooks
3. Datapane reports to track accuracy automatically generated (low priority TBD)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/FriendlyUser/intraday_ta.git/feature/setup-volia?filepath=intraday_ta.ipynb)

### Setup

```bash
./install.sh
```

Set python interpreter to
```
/home/codespace/.conda/envs/myenv/bin/python3
```

