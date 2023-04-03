import gym

# Agent Policies
def policy(obs):
    return 0

def random_action_policy(obs, action_space):
    return action_space.sample()

# print off the observation values in an easy-to-read way
def pretty_print_obs(obs, digit_count):
    new_list = []
    for num in obs:
        new_list.append(round(num, digit_count))
    return new_list

# Simulate the agent behavior in the selected environment
def simulate_verbose(env, rap, seed):
    
    observation, info = env.reset(seed=seed)
    terminated = False
    tick = 0
    total_reward = 0

    while terminated == False:
        print(f"Episode Step: {tick}")
        action = random_action_policy(observation, env.action_space)
        print(f"\t Action: {action}")
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward+= reward
        print(f"\t Obs: {pretty_print_obs(observation, 4)}")
        print(f"\t Reward: {reward}")
        print(f"\t Total Reward: {reward}")
        print(f"\t Terminated: {terminated}")
        print(f"\t Truncated: {truncated}")
        print(f"\t Info: {info}")

        if terminated or truncated:
            observation, info = env.reset()
        
        tick+=1
    env.close()
    return total_reward

# Run the main function
if __name__ == "__main__":
    env = gym.make("LunarLander-v2")
    total_reward = simulate_verbose(env, random_action_policy, seed=42)
    print(f"total reward: {total_reward}")
    
