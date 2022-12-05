# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:18:24 2021

@author: SYEDIHTESHAMHUSSAINS
"""

import numpy as np 
import DTR_Environment as DTR
actions = ('PSY' , 'MED', 'TM', 'PSY+MED')
states = ['S_0', 'S_1' , 'S_2','S_3','S_4', 'Success' , 'Failure' ]
n_trajectories=8
trajectory_length=2


    
def main():
    discount=0.01
    n_actions = len(actions)
    n_states =  len(states)
    dtr=DTR.Dynamic_Treatment_Regime(discount)
    
    Parameter= dtr.RandomParameter( )
    
        
    Input_Parameter= Parameter[0]
    
    print('___________________________________________________________________________________')
    print('Input_Parameter=', Input_Parameter,'   STATE...ACTION...STATE...ACTION...FINAL-STATE')
    print('___________________________________________________________________________________')
    
    a=[n_states,n_actions,n_states] 
    Q_table= Da = Dc= np.zeros(a) 
    for i in range(n_states):
        for j in range(n_actions):
            Q_table[i,j]=np.random.dirichlet(np.ones(7)*1000.,size=1)
    
    #Q_table[0,:]=[0.5,0.5,0,0]
    Trajectories_P, Trajectories_N = dtr.generate_trajectories(Input_Parameter, 
                                                               trajectory_length, 
                                                               n_trajectories )
    print('Positive_Trajectories')
    for i in range(n_trajectories):
            print('          ', i , '                        ',states[Trajectories_P[i,0,0]],
                  '...',actions[Trajectories_P[i,0,1]],
                  '...', states[Trajectories_P[i,0,2]],
                  '...',actions[Trajectories_P[i,1,1]],
                  '......',states[Trajectories_P[i,1,2]])
    print('-----------------------------------------------------------------------------------')        
    print('Negative_Trajectories')       
    for i in range(n_trajectories):
            print('          ', i , '                        ',states[Trajectories_N[i,0,0]],
                  '...',actions[Trajectories_N[i,0,1]],
                  '...', states[Trajectories_N[i,0,2]],
                  '...',actions[Trajectories_N[i,1,1]],
                  '......',states[Trajectories_N[i,1,2]])
            
    Trajectories_Random= dtr.new_generate_trajectories(n_trajectories, 
                                                       trajectory_length, Q_table,
                                        random_start=False)
    
    print('-----------------------------------------------------------------------------------')
    print('Initial learned_Trajectories')
    for i in range(n_trajectories):
            print('          ', i , '                        ',states[Trajectories_Random[i,0,0]],
                  '...',actions[Trajectories_Random[i,0,1]],
                  '...', states[Trajectories_Random[i,0,2]],
                  '...',actions[Trajectories_Random[i,1,1]],
                  '......',states[Trajectories_Random[i,1,2]])
            
    w=[n_states,n_actions,n_states]
    postive_Prob= nagetive_prob= random_prob = np.zeros(w)
    
                   
    random1=Trajectories_P.tolist() 
    random2=Trajectories_N.tolist() 
    
    
    def Prob_calculator(random_num,n_trajectories,i,j,k):
        a=[i,j,k]
        count1=sum(x.count( a ) for x in random_num)
        return count1/n_trajectories
        
    
        
    postive_Prob = np.array(
                [[[Prob_calculator(random1,n_trajectories,i, j, k)
                   for k in range(n_states)]
                  for j in range(n_actions)]
                 for i in range(n_states)])
    
    nagetive_prob=np.array(
                [[[Prob_calculator(random2,n_trajectories,i, j, k)
                   for k in range(n_states)]
                  for j in range(n_actions)]
                 for i in range(n_states)])
    
    a=[n_states,n_actions]
    for _ in range (10):
        random3=Trajectories_Random.tolist()
        random_prob=np.array(
                    [[[Prob_calculator(random3,n_trajectories,i, j, k)
                       for k in range(n_states)]
                      for j in range(n_actions)]
                     for i in range(n_states)])
        
        Q_Table=np.zeros(a)
        
        Da= postive_Prob/(postive_Prob+random_prob)
        
        Dc=(postive_Prob+random_prob)/(postive_Prob + random_prob + nagetive_prob)
        
        Da[np.isnan(Da)] = 0 # 0/0 generates Nan "so this function is used to replace nan with zero" 
        Dc[np.isnan(Dc)] = 0
        
        Q_Values=Da+Dc
        
        for i in range(n_states):
            for j in range(n_actions):
                Q_Table[i,j]=sum(Q_Values[i,j,:])
                
        Trajectories_Random= dtr.new_generate_trajectories(n_trajectories, 3, Q_Table,
                                            random_start=False)
    
    
    
   
    
    
    print('-----------------------------------------------------------------------------------')
    print('Final learned_Trajectories')
    for i in range(n_trajectories):
            print('          ', i , '                        ',states[Trajectories_Random[i,0,0]],
                  '...',actions[Trajectories_Random[i,0,1]],
                  '...', states[Trajectories_Random[i,0,2]],
                  '...',actions[Trajectories_Random[i,1,1]],
                  '......',states[Trajectories_Random[i,1,2]])
    print('___________________________________________________________________________________')        
            
if __name__ == "__main__":
  main()