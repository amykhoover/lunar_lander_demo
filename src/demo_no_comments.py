import gym


def policy(obs):
    return 0

def random_action_policy(obs, action_space):
    return action_space.sample()


def pretty_print_obs(obs, digit_count):
    new_list = []
    for num in obs:
        new_list.append(round(num, digit_count))
    return new_list


def simulate(env, rap, seed):
    
    observation, info = env.reset(seed=seed)
    done = False
    total_reward = 0

    while not done:
        action = random_action_policy(observation, env.action_space)
        observation, reward, done, truncated, info = env.step(action)
        total_reward+= reward
       

        if done or truncated:
            observation, info = env.reset()
        
    env.close()

    return total_reward


if __name__ == "__main__":
    env = gym.make("LunarLander-v2")
    total_reward = simulate(env, random_action_policy, seed=42)
    print(f"total reward: {total_reward}")
    
