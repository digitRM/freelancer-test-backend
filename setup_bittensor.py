import bittensor
wallet = bittensor.wallet()
wallet.create_new_coldkey()
wallet.create_new_hotkey()
print (wallet)
