ADDRESS = '0.0.0.0'
PORT = 5050

class Debugger:

    @staticmethod
    def enable_debugger_attach():
        try:
            import ptvsd
            
            ptvsd.enable_attach(address=(ADDRESS,PORT), redirect_output=True)
            print(f'Debugger attach enabled (PTVSD)! Running on {ADDRESS}:{PORT}.')
        except Exception as exception:
            print(f"Debugger attach couldn't be enabled. Error: {exception}")
