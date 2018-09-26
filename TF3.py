### variable

import tensorflow as tf

# define variable state
state = tf.Variable(0, name='counter')

# 定义常量 one
one = tf.constant(1)

# 定义加法步骤 (注: 此步并没有直接计算)
new_value = tf.add(state, one)

# 将 State 更新成 new_value
update = tf.assign(state, new_value)


# 如果定义 Variable, 就一定要 initialize
init = tf.global_variables_initializer()

# 使用 Session
with tf.Session() as sess:
    sess.run(init)  #激活init
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))


## 1， 2， 3