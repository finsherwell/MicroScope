.PHONY: setup test format run

setup:
	python -m venv .venv
	.venv/Scripts/activate && pip install -e .

test:
	pytest tests/

format:
	black .

run:
	microanalyse --input sample.csv --outdir ./output --visuals --summary