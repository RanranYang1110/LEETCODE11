#-*- coding:utf-8 -*-
# @author: qianli
# @file: asteroidCollision.py
# @time: 2019/11/04
def asteroidCollision(asteroids):
    '''行星碰撞'''
    stack = []
    for s in asteroids:
        while stack and s < 0 and stack[-1] > 0:
            if stack[-1] == -1 * s:
                stack.pop()
            elif stack[-1] < -1 * s:
                stack.pop()
                continue
            break
        else:
            stack.append(s)
    return stack
asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))

asteroids = [3, 2, -5]
print(asteroidCollision(asteroids))

asteroids = [-2, -1, 1, 2]
print(asteroidCollision(asteroids))