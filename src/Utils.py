import argparse
import os

class Utils: 
    @staticmethod
    def retrieve_token(): 
        print("Utils::retrieve_token() : trying to get token from command line arguments...")
        parser = argparse.ArgumentParser("EveSight")
        parser.add_argument("-token", help="Provide the token for the bot.", type=str, required=False, default="UNDEFINED")
        args = parser.parse_args()
        if args.token != "UNDEFINED":
            print("Utils::retrieve_token() : token is successfully retrieved.")
            return args.token
        print("Utils::retrieve_token() : trying to get token from environment variables...")
        token = os.getenv('EVESIGHT_TOKEN', "UNDEFINED")
        if token == "UNDEFINED":
            raise Exception("Utils::retrieve_token() : failed to retrieve the token.")
        else:
            print("Utils::retrieve_token() : token is retrieved successfully.")
            return token