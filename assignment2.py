import numpy as np
import random
INITIAL_STATE='sunny'
class WeatherSimulation:
    transition_probabilities={}
    holding_times={}
    current_state_str=''
    list_to_iterate=[]
    idx=-1
    hld_time=0;
    def __init__(self,transition_probabilities:dict,holding_times:dict):
        self.transition_probabilities=transition_probabilities
        self.holding_times=holding_times
        self.current_state_str=INITIAL_STATE
        for key in transition_probabilities:
            ans=0
            for key2 in transition_probabilities[key]:
                ans+=transition_probabilities[key][key2]
            if(ans>1.0):
                raise RuntimeError("the sum of probabilities is  not equal to 1")
    
    def get_states(self):
        return_list=[]
        for key in self.transition_probabilities:
            return_list.append(key)
        return return_list
    
    def current_state(self):
        return self.current_state_str
    

    def next_state(self):
        self.hld_time+=1
        if(self.holding_times[self.current_state_str]==self.hld_time):
            self.current_state_str = np.random.choice(
                list(self.transition_probabilities.keys()),
                 p = list(self.transition_probabilities[self.current_state_str].values()))
            self.hld_time=0
        return self.current_state_str
    


    def set_state(self,new_state_str):
        self.current_state_str=new_state_str



    def iterable(self):
        i=0
        while i<=1:
            self.next_state()
            yield self.current_state_str
    
    def next_state_str(self):
        self.current_state_str = np.random.choice(
                list(self.transition_probabilities.keys()),
                 p = list(self.transition_probabilities[self.current_state_str].values()))
        return self.current_state_str

      
    def simulate(self,hours):
        dict_per={
            'sunny':0, 'cloudy':0, 'rainy':0, 'snowy':0
        }
        total=0
        while hours>0:
            dict_per[self.current_state_str]+=1
            total+=1
            hours-=self.holding_times[self.current_state_str];
            self.current_state_str=self.next_state()
        list_ans=[]
        for key in dict_per:
            print(dict_per[key],total)
            list_ans.append((dict_per[key]/total)*100)
        return list_ans

    def current_state_remaining_hours(self):
        return self.holding_times[self.current_state_str]-self.hld_time


# my_transitions = {
# 'sunny':{'sunny':0.7, 'cloudy':0.3, 'rainy':0, 'snowy':0},
# 'cloudy':{'sunny':0.5, 'cloudy': 0.3, 'rainy':0.15, 'snowy':0.05},
# 'rainy':{'sunny':0.6, 'cloudy':0.2, 'rainy':0.15, 'snowy':0.05},
# 'snowy':{'sunny':0.6, 'cloudy':0.2, 'rainy':0.05, 'snowy':0.15}
# }
# my_holding_times = {'sunny':1, 'cloudy':2, 'rainy':2, 'snowy':1}

# obj=WeatherSimulation(my_transitions,my_holding_times)
# print(obj.get_states())

# print(obj.next_state())

# print(obj.next_state())