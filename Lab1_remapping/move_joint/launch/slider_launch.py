from simple_launch import SimpleLauncher

def generate_launch_description():
    sl = SimpleLauncher()
    
    sl.declare_arg('name', default_value='right_e0')
    
    sl.node('slider_publisher', 'slider_publisher', arguments = [sl.find('move_joint', 'single_joint.yaml')], name=sl.arg('name'))
    
    sl.node('move_joint', 'move_joint', parameters={'joint_name': sl.arg('name')}, remappings = {'joint_setpoint' : 'setpoint'}.items())
    
    
    
    return sl.launch_description() 
