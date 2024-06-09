"""
    -No need to run again, most of free the data has been gnerated 
"""

from leetscrape import GenerateCodeStub
from leetscrape import ExtractSolutions
import os,json

save_dir = './codeStub/q_0001_twoSum.py'
json_file_name = './json/questions.json'

def Exract_all_Solutions(json_file_name):
    """
    -read all non paid problems
    -extract all titleslug
    -use each titleslug as mkdir 
    """
    
    with open(json_file_name, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)

    filtered_items = [item for item in json_data if item["paidOnly"] == "False"]

    err_data_list = []
    for items in filtered_items:
        titelslug = items["titleSlug"]
        print(titelslug)
        custom_dir = f'./codeStub/{titelslug}'
        try:
            os.mkdir(custom_dir)
            try:
                fcs = GenerateCodeStub(titleSlug=titelslug)
                fcs.generate(directory=custom_dir)
            except Exception as e:
                err_data_list.append(titelslug)
                print("err while solution") 
            # break
        except Exception as e:
            print(f"Err while creating folder.{e}")
           
    print(f"Completed. error list : {err_data_list}")            
            
Exract_all_Solutions(json_file_name)


# errored data while generating solutions
# ['remove-duplicates-from-sorted-array', 'remove-element', 'valid-sudoku', 'combination-sum-ii', 'merge-intervals', 'remove-duplicates-from-sorted-array-ii', 'binary-tree-inorder-traversal', 'unique-binary-search-trees-ii', 'validate-binary-search-tree', 'recover-binary-search-tree', 'same-tree', 'symmetric-tree', 'binary-tree-level-order-traversal', 'binary-tree-zigzag-level-order-traversal', 'maximum-depth-of-binary-tree', 'construct-binary-tree-from-preorder-and-inorder-traversal', 'construct-binary-tree-from-inorder-and-postorder-traversal', 'binary-tree-level-order-traversal-ii', 'convert-sorted-array-to-binary-search-tree', 'convert-sorted-list-to-binary-search-tree', 'balanced-binary-tree', 'minimum-depth-of-binary-tree', 'path-sum', 'path-sum-ii', 'flatten-binary-tree-to-linked-list', 'populating-next-right-pointers-in-each-node', 'populating-next-right-pointers-in-each-node-ii', 'binary-tree-maximum-path-sum', 'clone-graph', 'copy-list-with-random-pointer', 'linked-list-cycle-ii', 'binary-tree-preorder-traversal', 'binary-tree-postorder-traversal', 'lru-cache', 'min-stack', 'intersection-of-two-linked-lists', 'binary-search-tree-iterator', 'combine-two-tables', 'second-highest-salary', 'nth-highest-salary', 'rank-scores', 'consecutive-numbers', 'employees-earning-more-than-their-managers', 'duplicate-emails', 'customers-who-never-order', 'department-highest-salary', 'department-top-three-salaries', 'reverse-bits', 'delete-duplicate-emails', 'rising-temperature', 'binary-tree-right-side-view', 'number-of-islands', 'implement-trie-prefix-tree', 'design-add-and-search-words-data-structure', 'implement-stack-using-queues', 'kth-smallest-element-in-a-bst', 'implement-queue-using-stacks', 'lowest-common-ancestor-of-a-binary-search-tree', 'lowest-common-ancestor-of-a-binary-tree', 'delete-node-in-a-linked-list', 'binary-tree-paths', 'trips-and-users', 'peeking-iterator', 'find-median-from-data-stream', 'serialize-and-deserialize-binary-tree', 'longest-increasing-subsequence', 'range-sum-query-immutable', 'range-sum-query-2d-immutable', 'range-sum-query-mutable', 'house-robber-iii', 'flatten-nested-list-iterator', 'data-stream-as-disjoint-intervals', 'design-twitter', 'insert-delete-getrandom-o1', 'insert-delete-getrandom-o1-duplicates-allowed', 'linked-list-random-node', 'shuffle-an-array', 'longest-absolute-file-path', 'random-pick-index', 'sum-of-left-leaves', 'construct-quad-tree', 'n-ary-tree-level-order-traversal', 'flatten-a-multilevel-doubly-linked-list', 'all-oone-data-structure', 'path-sum-iii', 'string-compression', 'serialize-and-deserialize-bst', 'delete-node-in-a-bst', 'lfu-cache', 'implement-rand10-using-rand7', 'generate-random-point-in-a-circle', 'random-point-in-non-overlapping-rectangles', 'find-mode-in-binary-search-tree', 'game-play-analysis-i', 'find-bottom-left-tree-value', 'find-largest-value-in-each-tree-row', 'random-flip-matrix', 'random-pick-with-weight', 'minimum-absolute-difference-in-bst', 'encode-and-decode-tinyurl', 'convert-bst-to-greater-tree', 'game-play-analysis-iv', 'reverse-words-in-a-string-iii', 'logical-or-of-two-binary-grids-represented-as-quad-trees', 'maximum-depth-of-n-ary-tree', 'binary-tree-tilt', 'managers-with-at-least-5-direct-reports', 'subtree-of-another-tree', 'employee-bonus', 'find-customer-referee', 'investments-in-2016', 'customer-placing-the-largest-number-of-orders', 'n-ary-tree-preorder-traversal', 'n-ary-tree-postorder-traversal', 'big-countries', 'classes-more-than-5-students', 'human-traffic-of-stadium', 'friend-requests-ii-who-has-the-most-friends', 'construct-string-from-binary-tree', 'sales-person', 'tree-node', 'triangle-judgement', 'merge-two-binary-trees', 'biggest-single-number', 'not-boring-movies', 'design-circular-queue', 'add-one-row-to-tree', 'exchange-seats', 'swap-salary', 'average-of-levels-in-binary-tree', 'design-circular-deque', 'find-duplicate-subtrees', 'two-sum-iv-input-is-a-bst', 'maximum-binary-tree', 'print-binary-tree', 'maximum-width-of-binary-tree', 'trim-a-binary-search-tree', 'second-minimum-node-in-a-binary-tree', 'implement-magic-dictionary', 'map-sum-pairs', 'longest-univalue-path', 'employee-importance', 'insert-into-a-binary-search-tree', 'kth-largest-element-in-a-stream', 'design-hashset', 'design-hashmap', 'design-linked-list', 'random-pick-with-blacklist', 'range-module', 'maximum-length-of-repeated-subarray', 'my-calendar-i', 'my-calendar-ii', 'my-calendar-iii', 'prefix-and-suffix-search', 'minimum-distance-between-bst-nodes', 'binary-tree-pruning', 'guess-the-word', 'exam-room', 'all-nodes-distance-k-in-binary-tree', 'smallest-subtree-with-all-the-deepest-nodes', 'leaf-similar-trees', 'all-possible-full-binary-trees', 'maximum-frequency-stack', 'increasing-order-search-tree', 'rle-iterator', 'online-stock-span', 'online-election', 'complete-binary-tree-inserter', 'number-of-recent-calls', 'range-sum-of-bst', 'flip-equivalent-binary-trees', 'check-completeness-of-a-binary-tree', 'univalued-binary-tree', 'binary-tree-cameras', 'time-based-key-value-store', 'vertical-order-traversal-of-a-binary-tree', 'smallest-string-starting-from-leaf', 'cousins-in-binary-tree', 'maximum-binary-tree-ii', 'construct-binary-search-tree-from-preorder-traversal', 'maximum-difference-between-node-and-ancestor', 'recover-a-tree-from-preorder-traversal', 
# 'stream-of-characters', 'binary-search-tree-to-greater-sum-tree', 'customers-who-bought-all-products', 'actors-and-directors-who-cooperated-at-least-three-times', 'product-sales-analysis-i', 'product-sales-analysis-iii', 'project-employees-i', 'insufficient-nodes-in-root-to-leaf-paths', 'sales-analysis-iii', 'delete-nodes-and-return-forest', 'print-in-order', 'print-foobar-alternately', 'print-zero-even-odd', 'building-h2o', 'lowest-common-ancestor-of-deepest-leaves', 'user-activity-for-the-past-30-days-i', 'snapshot-array', 'article-views-i', 'online-majority-element-in-subarray', 'market-analysis-i', 'maximum-level-sum-of-a-binary-tree', 'product-price-at-a-given-date', 'dinner-plate-stacks', 'immediate-food-delivery-ii', 'reformat-department-table', 'monthly-transactions-i', 'fizz-buzz-multithreaded', 'last-person-to-fit-in-the-bus', 'design-skiplist', 'minimum-moves-to-reach-target-with-rotations', 'queries-quality-and-percentage', 'the-dining-philosophers', 'average-selling-price', 'number-of-closed-islands', 'find-elements-in-a-contaminated-binary-tree', 'minimum-moves-to-move-a-box-to-their-target-location', 'count-square-submatrices-with-all-ones', 'students-and-examinations', 'iterator-for-combination', 'deepest-leaves-sum', 'all-elements-in-two-binary-search-trees', 'sum-of-nodes-with-even-valued-grandparent', 'restaurant-growth', 'delete-leaves-with-a-given-value', 'list-the-products-ordered-in-a-period', 'the-k-weakest-rows-in-a-matrix', 'maximum-product-of-splitted-binary-tree', 'movie-rating', 'tweet-counts-per-frequency', 'maximum-students-taking-exam', 'product-of-the-last-k-numbers', 'apply-discount-every-n-orders', 'linked-list-in-binary-tree', 'longest-zigzag-path-in-a-binary-tree', 'maximum-sum-bst-in-binary-tree', 'replace-employee-id-with-the-unique-identifier', 'find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree', 'design-a-stack-with-increment-operation', 'balance-a-binary-search-tree', 'capital-gainloss', 'design-underground-system', 'top-travellers', 'minimum-time-to-collect-all-apples-in-a-tree', 'consecutive-characters', 'count-good-nodes-in-binary-tree', 'pseudo-palindromic-paths-in-a-binary-tree', 'design-browser-history', 'subrectangle-queries', 'kth-ancestor-of-a-tree-node', 'group-sold-products-by-the-date', 'find-users-with-valid-e-mails', 'patients-with-a-condition', 'number-of-good-leaf-nodes-pairs', 'matrix-diagonal-sum', 'customer-who-visited-but-did-not-make-any-transactions', 'bank-account-summary-ii', 'throne-inheritance', 'design-parking-system', 'find-valid-matrix-given-row-and-column-sums', 'even-odd-tree', 'fancy-sequence', 'percentage-of-users-attended-a-contest', 'design-an-ordered-stream', 'average-time-of-process-per-machine', 'fix-names-in-a-table', 'design-front-middle-back-queue', 'invalid-tweets', 'daily-leads-and-partners', 'number-of-students-unable-to-eat-lunch', 'find-followers-count', 'the-number-of-employees-which-report-to-each-employee', 'find-total-time-spent-by-each-employee', 'recyclable-and-low-fat-products', 'primary-department-for-each-employee', 'rearrange-products-table', 'design-authentication-manager', 'finding-mk-average', 'frequency-of-the-most-frequent-element', 'seat-reservation-manager', 'rotating-the-box', 'finding-pairs-with-a-certain-sum', 'calculate-special-bonus', 'the-latest-login-in-2020', 'count-salary-categories', 'design-movie-rental-system', 'build-array-from-permutation', 'longest-common-subpath', 'merge-bsts-to-create-single-bst', 'confirmation-rate', 
# 'employees-with-missing-information', 'employees-whose-manager-left-the-company', 'operations-on-tree', 'detect-squares', 'maximum-difference-between-increasing-elements', 'stock-price-fluctuation', 'simple-bank-system', 'walking-robot-simulation-ii', 'maximum-number-of-tasks-you-can-assign', 'two-furthest-houses-with-different-colors', 'range-frequency-queries', 'removing-minimum-and-maximum-from-array', 'step-by-step-directions-from-a-binary-tree-node-to-another', 'sequentially-ordinal-rank-tracker', 'design-bitset', 'create-binary-tree-from-descriptions', 'encrypt-and-decrypt-strings', 'design-an-atm-machine', 'intersection-of-multiple-arrays', 'k-divisible-elements-subarrays', 'count-nodes-equal-to-average-of-subtree', 'count-integers-in-intervals', 'booking-concert-tickets-in-groups', 'design-a-text-editor', 'evaluate-boolean-binary-tree', 'smallest-number-in-infinite-set', 'design-a-number-container-system', 'design-a-food-rating-system', 'number-of-unique-subjects-taught-by-each-teacher', 'amount-of-time-for-binary-tree-to-be-infected', 'longest-uploaded-prefix', 'height-of-binary-tree-after-subtree-removal-queries', 'minimum-number-of-operations-to-sort-a-binary-tree-by-level', 'closest-nodes-queries-in-a-binary-search-tree', 'design-memory-allocator', 'find-consecutive-integers-from-a-data-stream', 'left-and-right-sum-differences', 'kth-largest-sum-in-a-binary-tree', 'check-if-object-instance-of-class', 'array-prototype-last', 'cache-with-time-limit', 'snail-traversal', 'flatten-deeply-nested-array', 'debounce', 'function-composition', 'group-by', 'filter-elements-from-array', 'apply-transform-over-each-element-in-array', 'cousins-in-binary-tree-ii', 'design-graph-with-shortest-path-calculator', 'allow-one-function-call', 'create-hello-world-function', 'frequency-tracker', 'find-the-losers-of-the-circular-game', 'neighboring-bitwise-xor', 'return-length-of-arguments-passed', 'to-be-or-not-to-be', 'compact-object', 'timeout-cancellation', 'execute-asynchronous-functions-in-parallel', 'join-two-arrays-by-id', 'sort-by', 'interval-cancellation', 'is-object-empty', 'create-a-dataframe-from-list', 'get-the-size-of-a-dataframe', 'display-the-first-three-rows', 'select-data', 'drop-duplicate-rows', 'drop-missing-data', 'modify-columns', 'rename-columns', 'change-data-type', 'fill-missing-data', 'reshape-data-concatenate', 'reshape-data-melt', 'method-chaining', 'minimum-sum-of-values-by-dividing-array', 'minimum-number-of-chairs-in-a-waiting-room', 'count-days-without-meetings', 'lexicographically-minimum-string-after-removing-stars', 'find-subarray-with-bitwise-and-closest-to-k']