import numpy as np
#Learns which model to select 


class ContexualBandit:
    def __init__(self, num_models, num_features, epsilon=0.1, learning_rate=0.01):
        self.num_models=num_models
        self.num_features=num_features
        self.epsilon=epsilon
        self.learning_rate=learning_rate

        self.weights=np.zeros((num_models, num_features))

        self.model_counts=np.zeros(num_models)
    
    #Select a model using epsilon-greedy
    def select_model(self, context):
        #Exploration: randomly select a model
        if np.random.random() < self.epsilon:
            selected_model=np.random.randint(self.num_models)
        
        #Exploitation: select the model with the highest expected reward
        else:
            expected_rewards=np.dot(self.weights, context)
            selected_model=np.random.choice(np.flatnonzero(expected_rewards==expected_rewards.max()))

        #track how many times each model is selected
        self.model_counts[selected_model]+=1

        return selected_model

#Test the contextual bandit model selection
if __name__=="__main__":

        



#next steps
#initialize the contextual bandit
#implement epsilon-greedy model selection
#update weights using rewards
#test contexual bandit