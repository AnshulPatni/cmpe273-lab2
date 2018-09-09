from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.addition(calculator_pb2.AddRequest(val1=50, val2=100))
    print("Sum of 50 and 100 is {}".format(response.result))

if __name__ == '__main__':
    run()