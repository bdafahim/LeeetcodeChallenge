
def removeElement(nums, val:int) -> int:
        next = 0
        for i in range(len(nums)):
            if nums[i] is not val:
                nums[next] = nums[i]
                next += 1
        return next


print(removeElement([0,1,2,2,3,0,4,2], 2))
