from game.scripting.action import Action

# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):

    def __init__(self):
        super().__init__()
        self._actor_list = []

    def execute(self, cast, script):
        self._actor_list = cast.get_all_actors()
        for actor in self._actor_list:
            actor.move_next()