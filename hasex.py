
def make_state_machine(pattern):
    state_machine = {}
    prev_state = ['start']
    
    i = 0
    while i < len(pattern):
        c = pattern[i:i+1]
        if c == '*':
            print 'in *', prev_state
            for ps in prev_state:
                print 'in *:', ps
                add_state(state_machine, ps, ps, ps)
        elif c == '.':
            for ps in prev_state:
                add_state(state_machine, c, c, 'anything')
        elif c == '[':
            (options, i) = get_options(pattern, i)
            state_name = ''.join(options)
            for ps in prev_state:
                add_state(state_machine, ps, state_name, options)
            prev_state = [state_name]
        else:
            for ps in prev_state:
                add_state(state_machine, ps, c, c)
            prev_state = [c]
        i +=1
    for ps in prev_state:
        add_state(state_machine, ps, 'end', '')

    return state_machine

def add_state(sm, frm , to ,value):
    print frm, to, value
    if frm not in sm:
        sm[frm] = []

    data = (to, value)
    sm[frm].append(data)

def get_options(pattern, i):
    options = []
    if pattern[i:i+1] == '[':
        i += 1
        while pattern[i:i+1] != ']':
            options.append(pattern[i:i+1])
            i += 1

    return options, i
    
def has_next_state(possible_states, value):
    print possible_states, value
    for s in possible_states:
        # s[0]: to state name
        # s[1]: possible values for transition
        if value in s[1] or 'anything' in s[1]:
            return s[0]
    return None

def has_end(possible_states):
    for ps in possible_states:
        if ps[0] == 'end':
            return True
    return False

def run_string(sm, text):
    print 'run a string over the state machine'
    current_state = 'start'
    for c in text:
        next_state = has_next_state(sm[current_state], c)
        print next_state
        if next_state == None:
            return False
        else:
            current_state = next_state
    
    return has_end(sm[current_state])

if __name__ == '__main__':
    sm = make_state_machine("a[bc]*")
    print sm

    print run_string(sm, "abc")    