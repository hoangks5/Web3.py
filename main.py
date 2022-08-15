from web3 import Web3
import time, json
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())



address = '0x5e99EaB168414773F8298596dd126aFf131e3dad'
balance = web3.eth.get_balance(address)
print(balance)
 
result = web3.fromWei(balance,'ether')
print(result)