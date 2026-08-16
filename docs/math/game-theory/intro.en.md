author: cutekibry, woruo27, Backl1ght, c-forrest

**Game theory** is a branch of economics that mainly studies the various behaviors produced under specific rules by individuals with competitive or adversarial natures. Game theory focuses on the expected and actual behaviors of individuals in a game, and studies their optimal strategies.

Loosely speaking, game theory mainly studies: in a game, how the multiple players playing the game choose strategies.

## Basic concepts

This section briefly introduces some common concepts in game theory.

### Cooperative/non-cooperative games

A **cooperative game** is a game in which participants can form coalitions and cooperate with one another. In this kind of game, the non-cooperative behavior of an individual is often punished by some external mechanism. In contrast, in a **non-cooperative game** there is no such mechanism, so participants either cannot form coalitions, or can only maintain cooperation by relying on a credible threat mechanism.

Compared with cooperative games, the study of non-cooperative games is more systematic and mature. All games discussed in this article are non-cooperative games.

### Symmetric/asymmetric games

In a **symmetric game**, different participants obtain the same payoff when making the same behavior; that is, the payoff depends only on the behavior itself and is independent of the identity of the actor. A game that does not satisfy this condition is called an **asymmetric game**.

### Zero-sum/non-zero-sum games

Main page: [zero-sum game](./zero-sum-game.md)

A **zero-sum game** refers to a game in which, no matter what behaviors the parties take, the sum of all participants' payoffs is always zero. Zero-sum games usually discussed involve two participants, in which case one party's gain is necessarily the other party's loss. In contrast, a **non-zero-sum game** allows multiple parties to win together or lose together, including **positive-sum games** and **negative-sum games**, etc.

### Simultaneous/sequential games

In a **simultaneous game**, all participants make decisions simultaneously without knowing the others' choices. For example, rock-paper-scissors is a typical simultaneous game. This kind of game is often represented by a payoff matrix, and usually does not involve the concept of time.

In contrast is the **sequential game**, i.e. participants act in turn. It should be noted that a later actor can observe at least part of the behavior of earlier actors, otherwise the order would be meaningless. Sequential games are usually described with the help of a game tree.

### Perfect/imperfect information games

**Perfect information** means that when a participant makes a decision at any moment, they fully understand the occurrence of all prior events, including the initial state of the game. For example, chess and Go are perfect-information games; while mahjong and poker are imperfect-information games, because a player cannot know the others' hands. Perfect information is usually used to describe sequential games; since in a simultaneous game the players cannot know the actions the others are about to take, a simultaneous game is usually not considered a perfect-information game.

### Complete/incomplete information games

**Complete information** means that all participants have complete understanding of the structure of the game itself (including each party's available decisions and final payoffs), and this information is common knowledge. In contrast is the incomplete-information game, in which some elements of the game (such as an opponent's available decisions or payoff function) are unknown to the participants.

It is worth noting that "complete information" and "perfect information" are two independent concepts that do not include each other. For example, mahjong is a game of complete but imperfect information, because its rules and payoffs are public, but the tile information is not transparent; while some games with hidden objectives but whose behaviors are public throughout are games of perfect but incomplete information.

## Combinatorial game theory

In competitive programming, the most common type of game is the **combinatorial game**. This term usually refers to those games that are hard to solve due to the huge number of states. Precisely because general combinatorial games are quite complex, combinatorial game theory mainly focuses on the following type: games with two players acting in turn, perfect information, and no random factors. Chess, Go, etc. are all typical combinatorial games.

### Impartial combinatorial games

Main page: [impartial game](./impartial-game.md)

An **impartial game** refers to a combinatorial game satisfying the following conditions:

-   In any given state, the actions available to all participants are exactly the same, depending only on the current state and independent of identity;
-   The same state in the game cannot be reached multiple times, the game ends when a participant cannot act, and the game must end in a non-tie after finitely many steps.

Impartial games are always symmetric games.

### Partizan combinatorial games

Main page: [partizan game](./partizan-game.md)

The concept opposite to impartial games is the **partizan game**, i.e. the actions a participant can take in a given state depend on their identity. Most board games (such as international chess, Chinese chess, Go, Gomoku, etc.) are partizan games, because a participant can only operate their own pieces.

### Normal/misère games

In a combinatorial game, the usual winner is the participant who takes the last action before the game ends. This is called a **normal game**. Corresponding to it is the **misère game**, i.e. the participant who takes the last action before the game ends is the loser.

Both impartial and partizan combinatorial games can be normal or misère games.

## References

-   [Game theory - Wikipedia](https://en.wikipedia.org/wiki/Game_theory)
-   [Combinatorial game theory - Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_game_theory)
-   [Impartial game - Wikipedia](https://en.wikipedia.org/wiki/Impartial_game)
-   [Misère - Wikipedia](https://en.wikipedia.org/wiki/Mis%C3%A8re)
