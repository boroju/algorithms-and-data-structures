install_uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

uv_init:
	cd src && uv venv

uv_sync:
	cd src && uv sync

uv_update:
	cd src && uv lock --upgrade