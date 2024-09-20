from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

# INITIAL_PEERS = PUBLIC_INITIAL_PEERS
INITIAL_PEERS = ["/ip4/127.0.0.1/tcp/31337/p2p/QmTQzBrsF37833RgHz4qUZY3RGk9F2d3y5TKAHDX9LB6mM"]

MODELS = [
    ModelInfo(
        dht_prefix="Meta-Llama-3-1-405B-Instruct-hf",
        repository="meta-llama/Meta-Llama-3.1-405B-Instruct",
        num_blocks=126,
    ),
    ModelInfo(
        dht_prefix="mistralai/Mixtral-8x22B-Instruct-v0-1",
        repository="mistralai/Mixtral-8x22B-Instruct-v0.1",
        num_blocks=56,
    ),
]

UPDATE_PERIOD = 60
