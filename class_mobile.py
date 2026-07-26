class Mobile:
    def __init__(self,brand,model,battery):
        self.brand = brand
        self.model = model
        self.battery = battery
        
        
    def call(self,number):
        self.number = number
        print(f"Calling {self.number} ....")
        
    def charge(self):
        print(f"{self.battery} charging...")
        
dial = Mobile("Nokia","3310","Battery")

dial.call("9876543210")
dial.charge