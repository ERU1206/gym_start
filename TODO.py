# TODO Worker(from gym)
"""
test 1: random run
test 2: heuristic?
"""
 # from Gym
 # Worker (multi processing)

# TODO Trainer

 # sample
    # input |  None
    # run
    # output|  samples: Dict[str, torch.Tensor]
 # train
    # input |  samples: Dict[str, torch.Tensor]
    # forward
        # calculate loss
    # backward
        # optimizer step


# TODO Model
    # call
        # input |  obs:torch.Tensor
            # shape? (N,84,84,4)?
        # output|  pi: torch.Tensor , value: torch.Tensor
            # shape? pi(logit) (N,4)?, value: (N)?

# TODO Loss (함수)
"""
loss = policy loss + value loss + entropy bonus
"""
    # input  |  sampele: torch.Tensor
    # output |  loss: torch.Tensor