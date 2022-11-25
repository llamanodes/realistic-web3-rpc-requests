#!/bin/bash -eux

ctc setup --headless --overwrite --rpc-url "$CTC_RPC_URL" --rpc-chain-id "${CTC_RPC_CHAIN_ID:-1}" --skip-aliases
