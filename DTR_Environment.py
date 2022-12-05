# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:20:03 2021

@author: SYEDIHTESHAMHUSSAINS
"""

import numpy as np

class Dynamic_Treatment_Regime(object):


    def __init__(self, discount):


        self.actions = ('psy' , 'med', 'tm', 'psymed')
        self.n_actions = len(self.actions)
        self.states = ['s0', 's1' , 's2','s3','s4', 's5' , 's6' ]
        self.n_actions = len(self.actions)
        self.n_states =  len(self.states)
        self.discount = discount

  
        
    def RandomParameter(self):
        """
        Generate Random Parameters .
        """
        
        Parameters=[]
        sex, Location, Cultural_level = ['M', 'F'], ['O', 'D'], ['L', 'M', 'H']
        for i in range(len(sex)):
            for j in range(len(Location)):
                for k in range(len(Cultural_level)):
                    Parameters.append((sex[i],Location[j],Cultural_level[k]))
        return Parameters
        
    
    

    def optimal_policy(self, sx, sex, Location, Cultural_level):
        """
        The optimal policy for this DTR Environment.

        state_int: What state we are in. int.
        -> Action int.
        """

        if sx== 0:
            
            if (Cultural_level == 'H'):
                if np.random.choice(['Res', 'NR'], p=[0.8,0.2]) == 'Res' :
                   return 0,1
                return 0,2 
            if (Cultural_level == 'L') :
                if np.random.choice(['Res', 'NR'], p=[0.68,0.32]) == 'Res' :
                   return 1,3
                return 1,4
            
            if (Cultural_level == 'M') and (Location == 'D'):
                if np.random.choice(['Res', 'NR'], p=[0.68,0.32]) == 'Res' :
                    return 0,1
                return 0,2
            
            if (Cultural_level == 'M') and (Location == 'O'):
                if np.random.choice(['Res', 'NR'], p=[0.8,0.2]) == 'Res' :
                    return 1,3
                return 1,4
            
            
        elif sx==1:
            return 2,5
        
        
        elif sx==2:
                        
            if (Cultural_level == 'L') or (Cultural_level == 'M' and Location == 'O'):
               if np.random.choice(['med', 'psymed'], p=[0.3,0.7]) == 'med' :
                   return 1,5
            return 3,5
           
            
        elif sx==3:
            return 2,5   
        
        
        elif sx==4:
            if (Cultural_level == 'H') or (Cultural_level == 'M' and Location == 'D'):
               if np.random.choice(['psy', 'psymed'], p=[0.4,0.6]) == 'psy' :
                   return 0,5
            return 3,5
           
       
        
        else:
            return 2,5
        
    def Negative_policy(self, sx, sex, Location, Cultural_level):
        """
        The negetive Policy for this DTR Environment.

        state_int: What state we are in. int.
        -> Action int.
        """

        if sx== 0:
            
            if (Cultural_level == 'H'):
                zr = np.random.choice([0,1,2,3], p=[0.25,0.25,0.25,0.25])
                if zr==0:
                   return 1,3
                if zr==1:
                   return 1,4
                if zr==2:
                   return 1,1
                if zr==3:
                   return 1,2 
            if (Cultural_level == 'L') :
                if np.random.choice(['Res', 'NR'], p=[0.68,0.32]) == 'Res' :
                   return 0,1
                return 0,2
            
            if (Cultural_level == 'M') and (Location == 'D'):
                if np.random.choice(['Res', 'NR'], p=[0.68,0.32]) == 'Res' :
                    return 1,3
                return 1,4
            
            if (Cultural_level == 'M') and (Location == 'O'):
                if np.random.choice(['Res', 'NR'], p=[0.8,0.2]) == 'Res' :
                    return 0,1
                return 0,2
            
            
        elif sx==1:
            return 2,6
        
        
        elif sx==2:
                        
            if (Cultural_level == 'L') or (Cultural_level == 'M' and Location == 'O'):
               if np.random.choice(['med', 'psymed'], p=[0.3,0.7]) == 'med' :
                   return 1,6
            return 3,6
           
            
        elif sx==3:
            return 2,6   
        
        
        elif sx==4:
            if (Cultural_level == 'H') or (Cultural_level == 'M' and Location == 'D'):
               if np.random.choice(['psy', 'psymed'], p=[0.4,0.6]) == 'psy' :
                   return 0,6
            return 3,6
           
       
        
        else:
            return 3,6

    def generate_trajectories(self,Input_Parameter, trajectory_length, n_trajectories,
                                    random_start=False):
        """
        Generate n_trajectories trajectories with length trajectory_length,
        following the given policy.

        n_trajectories: Number of trajectories. int.
        trajectory_length: Length of an episode. int.
        policy: Map from state integers to action integers.
        random_start: Whether to start randomly (default False). bool.
        -> [[(state int, action int, reward float)]]
        """

        Exprt_trajectories = [] 
        Negative_trajectories=[]
        sex, Location, Cultural_level= Input_Parameter[0], Input_Parameter[1], Input_Parameter[2]
        for _ in range(n_trajectories):  
            trajectory_E = []
            trajectory_N = []
            sx=0; sx_N=0
            for j in range(trajectory_length):
                    
                    # Follow the given policy.
                action, next_sx = self.optimal_policy( sx, sex, Location, Cultural_level)
                if next_sx == 6:
                    while next_sx >5 :
                        action, next_sx = self.optimal_policy( sx, sex, Location, Cultural_level)
                                                                                    
                state_int = sx
                action_int= action 
                state_action= state_int, action_int, next_sx
                trajectory_E.append(state_action)
                sx = next_sx
                
               
                ######For negative policy
                
                action_N, next_sx_N = self.Negative_policy(sx_N, sex, Location, Cultural_level)
                
                state_action= sx_N, action_N,next_sx_N
                trajectory_N.append(state_action)
                sx_N = next_sx_N
                
                
            Exprt_trajectories.append(trajectory_E)
          
            Negative_trajectories.append(trajectory_N)
        
          
            
        
    
        return np.array(Exprt_trajectories), np.array(Negative_trajectories)
    
    def choose__new_state_action(self, sx , n_states, Q_table): 
        '''
        >>> aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
        >>> np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
        array(['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'],
        dtype='|S11')
        '''

         #action = rn.choice([0,1,2,3], p = [Q_table[sx, a]for a in range(self.n_actions)])
        number_list=Q_table[sx,:].tolist() 
        max_value=max(number_list)
        action=number_list.index(max_value)
        if sx==0: 
                if action==0:
                     if np.random.choice(['Res', 'NR'], p=[0.8,0.2]) == 'Res' :
                       return 1,0
                     else:
                         return 2,0
                if action==1:
                     if np.random.choice(['Res', 'NR'], p=[0.8,0.2]) == 'Res' :
                       return 3,1
                     else:
                         return 4,1
            
        if sx==1 or sx==3:
                if action==2:
                    if np.random.choice(['Res', 'NR'], p=[0.99,0.01]) == 'Res' :
                         return 5,2
                    else:
                         return 6,2

        if sx==2 :
            if action==1:
                    if np.random.choice(['Res', 'NR'], p=[0.99,0.01]) == 'Res' :
                         return 5,1
                    else:
                         return 6, 1
            if action==3:
                     if np.random.choice(['Res', 'NR'], p=[0.8,0.2]) == 'Res' :
                       return 5,3
                     else:
                         return 6,3
                         
        if sx==4:
            if action==0:
                    if np.random.choice(['Res', 'NR'], p=[0.99,0.01]) == 'Res' :
                         return 5,0
                    else:
                         return 6,0
            if action==3:
                     if np.random.choice(['Res', 'NR'], p=[0.8,0.2]) == 'Res' :
                       return 5,3
                     else:
                         return 6,3
        if sx==5 or sx==6:
            return sx, action
            
        return np.random.choice([0,1,2,3,4,5,6]) , np.random.choice([0,1,2,3])
    
    
    def new_generate_trajectories(self,n_trajectories, trajectory_length, Q_table,
                                    random_start=False):
        """
        Generate n_trajectories trajectories with length trajectory_length,
        following the given policy.

        n_trajectories: Number of trajectories. int.
        trajectory_length: Length of an episode. Q_table contains values and 
        hence guide the agent to take optimal action at each state: Whether 
        to start randomly (default False). bool.
        -> [[(state int, action int, next state int )]]
        """

        trajectories = []
        for _ in range(n_trajectories):

            sx=0

            trajectory = []
            for _ in range(trajectory_length):
                

                        
                next_sx , action = self.choose__new_state_action(sx , 
                                                                     self.n_states,
                                                                     Q_table)
                    
                state_int = sx
                action_int = action
                trajectory.append((state_int, action_int, next_sx))
                sx = next_sx
                

            trajectories.append(trajectory)
        #print('Rand Trajectroies',trajectories )
       
        return np.array(trajectories)
   

