from django.db import models
from django.db.models import Q

from pokemonAPI.utils.iterators_operations import sort_dictionary_descending_order


class PokemonStats(models.Model):
    pokemon = models.OneToOneField('Pokemon', null=False, on_delete=models.CASCADE, related_name='stats')
    hp = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField()
    sp_attack = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    sp_defense = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    total_points = models.PositiveSmallIntegerField()

    @staticmethod
    def get_best_base_total_stats_pokemon_for_generation(generation: str) -> list:
        return list(
            PokemonStats.objects.filter(pokemon__generation=generation)
            .order_by('-total_points')
        )

    @staticmethod
    def get_best_base_total_stats_pokemon_for_type(type: str) -> list:
        return list(
            PokemonStats.objects.filter(Q(pokemon__type_1=type) | Q(pokemon__type_2=type))
            .order_by('-total_points')
        )

    @staticmethod
    def get_best_base_total_stats_pokemon_for_generation_and_type(generation: str, type: str) -> list:
        return list(
            PokemonStats.objects.filter(
                Q(pokemon__type_1=type) | Q(pokemon__type_2=type),
                pokemon__generation=generation
            )
            .order_by('-total_points')
        )

    def to_dict(self):
        return {
            'pokemon': self.pokemon.name,
            "hp": self.hp,
            "attack": self.attack,
            "sp_attack": self.sp_attack,
            "defense": self.defense,
            "sp_defense": self.sp_defense,
            "speed": self.speed,
            "total_points": self.total_points
        }

    def get_descending_ordered_stats(self) -> {}:
        return sort_dictionary_descending_order({
            "hp": self.hp,
            "attack": self.attack,
            "sp_attack": self.sp_attack,
            "defense": self.defense,
            "sp_defense": self.sp_defense,
            "speed": self.speed,
            "total_points": self.total_points
        })