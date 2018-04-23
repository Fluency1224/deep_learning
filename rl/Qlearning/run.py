#########################################################################
# File Name: run.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Wed 18 Apr 2018 12:00:11 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
from env import Maze
from learn_brain import QLearningTable


def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
