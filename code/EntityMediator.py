from code.Destroyers import Destroyers
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity_list: list[Entity]):
        for ent in range(len(entity_list)):
            entity = entity_list[ent]
            if entity.rect.right <= 0:
                if isinstance(ent, Destroyers):
                    entity_list.remove(ent)

        # if isinstance(enti, Destroyers):
        #     if enti.rect.right <= 0:
        #         entity_list.remove(enti)

    @staticmethod
    def __verify_collision_entity(ent_1, ent_2):

        valid_interaction = False
        if isinstance(ent_1, Destroyers) and isinstance(ent_2, Player):
            valid_interaction = True
        elif isinstance(ent_1, Player) and isinstance(ent_2, Destroyers):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True:
            if (ent_1.rect.right >= ent_2.rect.left and
                    ent_1.rect.left <= ent_2.rect.right and
                    ent_1.rect.bottom >= ent_2.rect.top and
                    ent_1.rect.top <= ent_2.rect.bottom):
                return True

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity_list)
            for j in range(i + 1, len(entity_list)):
                entity_2 = entity_list[j]
                gameOver = EntityMediator.__verify_collision_entity(entity_1, entity_2)
                if gameOver:
                    return True
