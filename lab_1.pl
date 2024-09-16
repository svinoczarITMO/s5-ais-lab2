% FACTS (1):
% blocks
block(glass).
block(concrete).
block(bricks).

block(stone).
block(coal_ore).
block(iron_ore).
block(copper_ore).
block(lapis_lazuli_ore).
block(redstone_ore).
block(gold_ore).
block(diamond_ore).
block(emerald_ore).
block(ancient_debris_ore).
block(obsidian).
block(oak_leaves).
block(grass).
block(vines).
block(fern).


% FACTS (2):
% tools
tool(hand, 0).
tool(shears, 0).
tool(wooden_pickaxe, 1).
tool(golden_pickaxe, 2).
tool(stone_pickaxe, 3).
tool(iron_pickaxe, 4).
tool(diamond_pickaxe, 5).
tool(netherite_pickaxe, 6).

obtained_with_tool(stone, wooden_pickaxe).
obtained_with_tool(coal_ore, wooden_pickaxe).
obtained_with_tool(copper_ore, stone_pickaxe).
obtained_with_tool(lapis_lazuli_ore, stone_pickaxe).
obtained_with_tool(iron_ore, stone_pickaxe).
obtained_with_tool(gold_ore, iron_pickaxe).
obtained_with_tool(redstone_ore, iron_pickaxe).
obtained_with_tool(diamond_ore, iron_pickaxe).
obtained_with_tool(emerald_ore, iron_pickaxe).
obtained_with_tool(obsidian, diamond_pickaxe).
obtained_with_tool(ancient_debris_ore, diamond_pickaxe).
obtained_with_tool(oak_leaves, shears).
obtained_with_tool(grass, shears).
obtained_with_tool(vines, shears).
obtained_with_tool(fern, shears).



% RULES:

% Rule for better
pickaxe_is_better(Tool1, Tool2) :- 
    tool(Tool1, Level1), 
    tool(Tool2, Level2), 
    Level1 > Level2.

% Block can be obtained by shears.
obtained_by_shears(Block, Tool) :- 
    obtained_with_tool(Block, Tool).

% Block can be obtained with a pickaxe or a better tool.
obtained_by_pickaxe(Block, Tool) :- 
    obtained_with_tool(Block, Tool). % Directly using the tool

obtained_by_pickaxe2(Block, Tool) :- 
    obtained_with_tool(Block, MinimumTool), 
    pickaxe_is_better(Tool, MinimumTool). % Finding the better tool

is_natural(Block) :- 
    Block \= glass,
    Block \= bricks,
    Block \= concrete.

is_manmade(Block) :-
    Block == glass;
    Block == bricks;
    Block == concrete.



% % Check (tests)
% :- begin_tests(block_tests).
% test(obtained_by_pickaxe_iron) :- obtained_by_pickaxe(iron_ore, stone_pickaxe). % true
% test(obtained_by_pickaxe_obsidian) :- obtained_by_pickaxe(obsidian, diamond_pickaxe). % true
% test(obtained_by_pickaxe_diamond) :- obtained_by_pickaxe(diamond_ore, wooden_pickaxe). % false
% test(obtained_by_shears_oak) :- obtained_by_shears(oak_leaves, shears). % true
% test(obtained_by_shears_stone) :- obtained_by_shears(stone, shears). % false
% test(is_natural_grass) :- is_natural(grass). % true
% test(is_manmade_glass) :- is_manmade(glass). % true
% test(is_manmade_fern) :- is_manmade(fern). % false
% :- end_tests(block_tests).

% Run tests
% :- run_tests.