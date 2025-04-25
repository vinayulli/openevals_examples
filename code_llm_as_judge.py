from openevals.code.llm import create_code_llm_as_judge, CODE_CORRECTNESS_PROMPT
from dotenv import load_dotenv

load_dotenv()
evaluator = create_code_llm_as_judge(
    prompt=CODE_CORRECTNESS_PROMPT,
    model="openai:o3-mini",
    code_extraction_strategy="all_code",
)

# test case 1 

INPUTS = """
Rewrite the code below to be async:
```python
def _run_mypy(
    *,
    filepath: str,
    mypy_cli_args: list[str],
) -> Tuple[bool, str]:
    result = subprocess.run(
        [
            "mypy",
            *mypy_cli_args,
            filepath,
        ],
        capture_output=True,
    )
    return _parse_mypy_output(result.stdout)
```
"""

OUTPUTS = """
```python
async def _run_mypy_async(
    *,
    filepath: str,
    mypy_cli_args: list[str],
) -> Tuple[bool, str]:
    process = await subprocess.run(
        [
            "mypy",
            *mypy_cli_args,
            filepath,
        ],
    )
    stdout, _ = await process.communicate()

    return _parse_mypy_output(stdout)
```
"""

eval_result = evaluator(
    inputs=INPUTS,
    outputs=OUTPUTS
)

print("test case 1",eval_result)

## test case 2 

INPUTS = """ Rewrite the helper below so it is **truly asynchronous** using **aiohttp** and
`asyncio.gather`.  Preserve the behaviour and return type
`List[Tuple[str, int]]`.  Rename it to `fetch_all_async`.

```python

from typing import List, Tuple
import requests

def fetch_all(urls: List[str]) -> List[Tuple[str, int]]:
    \"\"\"Return a list of (url, status_code) pairs.\"\"\"
    results = []
    for url in urls:
        r = requests.get(url, timeout=10)
        results.append((url, r.status_code))
    return results
``` """

OUTPUTS = """

 ```python
from typing import List, Tuple
import aiohttp, asyncio

async def fetch_all_async(urls: List[str]) -> List[Tuple[str, int]]:
    async def _fetch(session: aiohttp.ClientSession, url: str) -> Tuple[str, int]:
        async with session.get(url, timeout=10) as resp:
            return url, resp.status

    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*[_fetch(session, u) for u in urls])
``` 
"""

eval_result = evaluator(inputs=INPUTS, outputs=OUTPUTS)
print("test case 2", eval_result)

# test case 3 

INPUTS = "Generate a sample code for creating a line plot using seaborn"
OUTPUTS = """
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dates = pd.date_range("2025-01-01", periods=10, freq="D")
df = pd.DataFrame({
    "date": dates,
    "sales":  (50 + 5 * np.arange(10)).astype(float),
    "visits": (200 + np.random.randint(-20, 20, size=10)).astype(float)
})

sns.set_theme(style="whitegrid")              # optional aesthetic
ax = sns.lineplot(data=df, x="date", y="sales", label="Daily Sales")
sns.lineplot(data=df, x="date", y="visits", label="Website Visits", ax=ax)

ax.set(
    title="Sales vs. Visits Over Time",
    xlabel="Date",
    ylabel="Count"
)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""

eval_result = evaluator(
    inputs = INPUTS, 
    outputs= OUTPUTS
)

print("test case 3", eval_result)