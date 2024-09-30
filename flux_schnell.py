$ pip install replicate
$ export REPLICATE_API_TOKEN=<paste-your-token-here>
import replicate

output = replicate.run(
    "black-forest-labs/flux-schnell",
    input={
        "prompt": "black forest gateau cake spelling out the words \"FLUX SCHNELL\", tasty, food photography, dynamic shot",
        "go_fast": True,
        "num_outputs": 1,
        "aspect_ratio": "1:1",
        "output_format": "webp",
        "output_quality": 80
    }
)
print(output)
