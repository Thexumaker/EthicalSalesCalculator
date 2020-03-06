from django.shortcuts import render
from django.http import HttpResponse
from calc.forms import OrderForm
from django.shortcuts import redirect

from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, "ethicalSalesCalc/test.html")
def orderForm(request):
    context = {}
    zz = {}
    context['form'] = OrderForm()
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            form.save(commit=True)


            spotColorDict = {"1C":[1.38,1.1,0.95,0.85,0.75,0.7], "2C":[1.63,1.28,1.1,0.95,0.85,0.8], "3C": [1.88,1.46,1.25,1.05,0.95,0.9],
            "4C":[2.13,1.64,1.4,1.15,1.05,1], "5C" :[2.38,1.82,1.55,1.25,1.15,1.1], "6C":[2.63,2,1.7,1.35,1.25,1.2],
            "7C":[2.88,2.18,1.85,1.45,1.35,1.3], "8C":[3.13,2.36,2,1.55,1.45,1.4],
            "9C": [3.38,2.54,2.15,1.65,1.55,1.5], "10C":[3.63,2.72,2.3,1.75,1.65,1.6], "11C":[3.88,2.9,2.45,1.85,1.75,1.7],
            "12C":[4.13,3.08,2.6,1.95,1.85,1.8], "13C":[4.38,3.26,2.75,2.05,1.95,1.9], "14C" : [4.63,3.44,2.9,2.15,2.05,2]}
            #Calculates printing var, which determines price per shirt based on quantity
            import math

            def ceil(x, s):
                return s * math.ceil(float(x)/s)
            def printingVar(quantity):
                #Returns a single value

                if quantity < 300:
                    return 0
                elif quantity >= 300 and quantity < 500:
                    return 1
                elif quantity >= 500 and quantity < 1000:
                    return 2
                elif quantity >= 1000 and quantity < 2000:
                    return 3
                elif quantity >= 2000 and quantity < 5000:
                    return 4
                else:
                    return 5

            def referenceCalculator(printingVar):
            #Calculates the referene sheet used to get price per shirt
            #Returns Dictionary
                reference = {}
                for k,v in spotColorDict.items():
                    reference.update({k:v[printingVar]})
                return reference
            def addC(str):
                #Bro if u can't understand this lord help u
                return str + "C"
            def subtotalPriceCalculator(listofLocations,white,reference):
                #Returns a dictionary of subtotal prices
                updatedList = []
                subtotaldict = {"Front":None, "Back":None,"Left":None, "Right": None}
                if white:
                    for l in listofLocations:
                        l +=1
                        l = addC(str(l))
                        updatedList.append(l)
                else:
                    for l in listofLocations:

                        l = addC(str(l))
                        updatedList.append(l)

                tempValue =0
                for k,v in subtotaldict.items():
                    print(subtotaldict)
                    print(tempValue)
                    print(updatedList)
                    subtotaldict.update({k:reference.get(updatedList[tempValue])})
                    tempValue +=1
                return subtotaldict

            def totalPriceCalculator(subtotal):
                totalPricePerShirt = 0
                for k,v in subtotal.items():
                    totalPricePerShirt += float(v)
                return totalPricePerShirt

            def screenCalculator(listofLocations,quantity, oversized):
                #Returns the total cost of screens
                screenCost =0
                if quantity > 1000:
                    screenCost = (oversized +1) * 32
                else:
                    for loc in listofLocations:
                        if loc != 0:
                            screenCost += (loc +1) *28
                    screenCost += (oversized +1) * 32
                return screenCost




            def flashCalculator(quantity,locations):
                #Returns total cost of flash
                #Returns a single value
                return .15 * quantity * locations
            def underMinCalc(quan,loc):
                if quan < 50:
                    return loc * 75
                else:
                    return 0
            def apparelTotalCost(listofSubtotals, locations,quantity):
                #calculates cost of apparel
                tshirt = sum(listofSubtotals)
                hoodie = tshirt + (.24 * locations * quantity)
                zipped = tshirt + (1 * locations * quantity)
                sleeve = tshirt + (.36 * locations * quantity)
                pants = tshirt + (1.36 * locations * quantity)
                priceDict = {"T-Shirts/Long-Sleeves Total":tshirt,
            "Hoodies/Crewnecks Total":hoodie,
            "Zipped Hoodies/Jackets/Windbreakers":zipped,
            "Printing on Sleeves/Pocket":sleeve,
            "Pants":pants}
                return priceDict
            def shippingWithTax(apparelChoice, clothesDict):
                costofChoice = clothesDict.get(apparelChoice)
                rush = round(costofChoice * 1.25 * 1.0925,2)
                superRush = round(costofChoice * 1.5 * 1.0925,2)
                normal = round(costofChoice * 1.0925,2)
                dict = {"Rush Shipping" : rush, "superRush": superRush, "Normal": normal}
                return dict
            numLocations = int(request.POST.get('numLocations', ''))
            nonWhiteApparel = request.POST.get('nonWhiteApparel', '')
            colorsF = int(request.POST.get('colorsF', ''))
            colorsB = int(request.POST.get('colorsB', ''))
            colorsR = int(request.POST.get('colorsR', ''))
            colorsL = int(request.POST.get('colorsL', ''))
            colorsSP = int(request.POST.get('colorsSP', ''))
            colorsOS = int(request.POST.get('colorsOS', ''))
            costPerItem = int(request.POST.get('costPerItem', ''))
            margin = 1.22
            quantity = int(request.POST.get('quantity', ''))

            printingVar = printingVar(quantity)
            reference = referenceCalculator(printingVar)
            subTotal = subtotalPriceCalculator([colorsF,colorsB,colorsR, colorsL], nonWhiteApparel, reference)
            totalPricePerShirt = totalPriceCalculator(subTotal)
            cartTotalCost = totalPricePerShirt * quantity
            flash = flashCalculator(quantity,numLocations)
            screenTotal = screenCalculator([colorsF,colorsB,colorsR, colorsL],quantity,colorsOS)
            underminCharge = underMinCalc(quantity,numLocations)
            ClothesDict = apparelTotalCost([cartTotalCost,flash,screenTotal,underminCharge],numLocations,quantity)
            withTaxandShipping = shippingWithTax("T-Shirts/Long-Sleeves Total", ClothesDict)
            screenPrintingPlusBlank = (quantity * costPerItem )+ withTaxandShipping.get("Normal")
            preCutomerTotal = screenPrintingPlusBlank * margin
            customerPricePerItem = ceil(preCutomerTotal/ quantity,0.25)
            customerSubTotal = customerPricePerItem *quantity
            print(subTotal)
            print(totalPricePerShirt)
            print(screenTotal)
            print(ClothesDict)
            print(withTaxandShipping)
            print(customerPricePerItem)
            print(customerSubTotal)

            content = {"numLocations": numLocations, "colorsF": colorsF, "colorsB": colorsB, "costPerItem": costPerItem, "quantity": quantity, "customerPricePerItem": customerPricePerItem, "customerSubTotal": customerSubTotal}
            return render(request, 'ethicalSalesCalc/TotalValues.html', content)
        else:
            print(form.errors)
    return render(request, 'ethicalSalesCalc/Order.html', context)
