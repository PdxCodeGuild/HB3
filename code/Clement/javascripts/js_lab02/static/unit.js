let inPut = document.getElementById('inPut')
        let reSult = document.getElementById('reSult')
        let inputType = document.getElementById('inputType')
        let resultType = document.getElementById('resultType')
        var inputTypeValue, resultTypeValue;

        inPut.addEventListener("keyup", myOutcome);
        inputType.addEventListener("change", myOutcome);
        resultType.addEventListener("change", myOutcome);

        inputTypeValue = inputType.value;
        resultTypeValue = resultType.value;

        function myOutcome() {

            inputTypeValue = inputType.value;
            resultTypeValue = resultType.value;
            


            if (inputTypeValue === "kilometer" && resultTypeValue === "meter") {
                reSult.value = Number(inPut.value) * 1000

            } else if (inputTypeValue === "meter" && resultTypeValue === "kilometer") {
                reSult.value = Number(inPut.value) * 0.001

            } else if (inputTypeValue === "meter" && resultTypeValue === "meter") {
                reSult.value = inPut.value

            } else if (inputTypeValue === "kilometer" && resultTypeValue === "kilometer") {
                reSult.value = inPut.value

            } else if (inputTypeValue === "kilometer" && resultTypeValue === "feet") {
                reSult.value = Number(inPut.value) * 3280.84

            } else if (inputTypeValue === "feet" && resultTypeValue === "kilometer") {
                reSult.value = Number(inPut.value) * 0.0003048

            }

            if (inputTypeValue === "meter" && resultTypeValue === "mile") {
                reSult.value = Number(inPut.value) * 0.0006214

            } else if (inputTypeValue === "mile" && resultTypeValue === "meter") {
                reSult.value = Number(inPut.value) * 1609.34

            } else if (inputTypeValue === "mile" && resultTypeValue === "mile") {
                reSult.value = inPut.value

            } else if (inputTypeValue === "mile" && resultTypeValue === "kilometer") {
                reSult.value = Number(inPut.value) * 1.60934

            } else if (inputTypeValue === "kilometer" && resultTypeValue === "mile") {
                reSult.value = Number(inPut.value) * 0.621371
            }


            if (inputTypeValue === "mile" && resultTypeValue === "feet") {
                reSult.value = Number(inPut.value) * 5280

            } else if (inputTypeValue === "feet" && resultTypeValue === "feet") {
                reSult.value = inPut.value

            } else if (inputTypeValue === "feet" && resultTypeValue === "mile") {
                reSult.value = Number(inPut.value) * 0.000189394

            } else if (inputTypeValue === "feet" && resultTypeValue === "meter") {
                reSult.value = Number(inPut.value) * 0.3048

            } else if (inputTypeValue === "meter" && resultTypeValue === "feet") {
                reSult.value = Number(inPut.value) * 3.28084
            }
        }
