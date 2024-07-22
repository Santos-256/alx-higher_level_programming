#!/usr/bin/node
exports.esrever = function (list) {
        /* Exporting a function named esrever
         * The function takes one parameter: list (the array to reverse)
         */
        let len = list.length - 1;
        let i = 0;
        // Swap elements starting from the beginning and end of the list, moving towards the middle
        while ((len - i) > 0) {
                const aux = list[len];
                list[len] = list[i];
                list[i] = aux;
                i++;
                len--;
        }
        return list;
};
