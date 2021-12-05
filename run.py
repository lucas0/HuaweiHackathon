import os, sys

cfilename = sys.argv[0]
cwd = os.path.abspath(cfilename+"/..")

data_dir = cwd+"/data"


#demand
#1,0
#2,10
#3,10
#4,10

#distance
#0.0,10.0,14.142135623730951,15.0
#10.0,0.0,10.0,25.0
#14.142135623730951,10.0,0.0,26.92582403567252
#15.0,25.0,26.92582403567252,0.0

#spec
#3,1,30

class Customer:
    def __init__(self, node_id, distances, demand):
        self.id = int(node_id)
        self.dists = [float(d) for d in distances]
        self.demand = demand
    def __str__(self):
        distances = "\n".join([str(d)+" to customer "+str(e)+"" for e,d in enumerate(self.dists)])
        return "Customer "+str(self.id)+" demands "+str(self.demand)+" and distances \n"+distances+"."

class Problem:

    def __init__(self, prob_id):
        self.id = prob_id
        self.customers = []
        self.load_problem()

    def load_problem(self):
        #load spec
        with open(data_dir+"/spec_"+str(self.id)+".txt", "r+") as f:
            num_customers, n_cars, capacity_car = f.readlines()[0].split(",")

        #load demand
        with open(data_dir+"/demand_"+str(self.id)+".txt", "r+") as f:
            demand_customers = [line[:-1].split(",")[1] for line in f.readlines()]

        #load distance
        with open(data_dir+"/distance_"+str(self.id)+".txt", "r+") as f:
            distances_customers = [line[:-1].split(",") for line in f.readlines()]

        for customer_id in range(int(num_customers)):
            self.customers.append(Customer(customer_id, distances_customers[customer_id], demand_customers[customer_id]))

    def generate_solutions(self):
        pass

p1 = Problem(1)
