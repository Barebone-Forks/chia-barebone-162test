from chia.consensus.default_constants import DEFAULT_CONSTANTS

test_constants = DEFAULT_CONSTANTS.replace(
    **{
        "MIN_PLOT_SIZE": 18,
        "MIN_BLOCKS_PER_CHALLENGE_BLOCK": 12,
        "DIFFICULTY_STARTING": 2**10,
        "DISCRIMINANT_SIZE_BITS": 16,
        "SUB_EPOCH_BLOCKS": 170,
        "WEIGHT_PROOF_THRESHOLD": 2,
        "WEIGHT_PROOF_RECENT_BLOCKS": 380,
        "DIFFICULTY_CONSTANT_FACTOR": 33554432,
        "NUM_SPS_SUB_SLOT": 16,  # Must be a power of 2
        "MAX_SUB_SLOT_BLOCKS": 50,
        "EPOCH_BLOCKS": 340,
        "BLOCKS_CACHE_SIZE": 340 + 3 * 50,  # Coordinate with the above values
        "SUB_SLOT_TIME_TARGET": 600,  # The target number of seconds per slot, mainnet 600
        "SUB_SLOT_ITERS_STARTING": 2**10,  # Must be a multiple of 64
        "NUMBER_ZERO_BITS_PLOT_FILTER": 1,  # H(plot signature of the challenge) must start with these many zeroes
        "MAX_FUTURE_TIME": 3600
        * 24
        * 10,  # Allows creating blockchains with timestamps up to 10 days in the future, for testing
        "COST_PER_BYTE": 1337,
        "MEMPOOL_BLOCK_BUFFER": 6,
    }
)
