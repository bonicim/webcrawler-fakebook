import queue

FAKEBOOK_LOGIN_URL = 'http://fring.ccs.neu.edu/accounts/login/?next=/fakebook/'
FAKEBOOK_DOMAIN_URL = 'http://fring.ccs.neu.edu'
NEXT_VAL = '/fakebook/'
VALUES_USERNAME = 'username'
VALUES_PASSWORD = 'password'
VALUES_NEXT = 'next'
VALUES_CSRF = 'csrfmiddlewaretoken'
NUM_THREADS = 10
q_frontier = queue.Queue()  # thread safe
q_flags = []
visited_set = frozenset()  # thread safe
total_loop_count = 0