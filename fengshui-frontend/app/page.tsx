"use client"
import React, { useEffect, useState } from 'react';

import { format, parse, isValid } from "date-fns"
import { cn } from "@/lib/utils"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { Input } from "@/components/ui/input"
import FengShuiResults from './components/fenshuiresults';
import { CalendarIcon } from "lucide-react"

export default function ZodiacReading() {
  const [fengShui, setFengShui] = useState(undefined);
  const [loading, setLoading] = useState(false);

  const [date, setDate] = React.useState<Date>()
  const [inputValue, setInputValue] = React.useState("")
  const [error, setError] = React.useState("")

  const handleDateSelect = (selectedDate: Date | undefined) => {
    setDate(selectedDate)
    setInputValue(selectedDate ? format(selectedDate, "MM/dd/yyyy") : "")
    setError("")
  }

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value
    setInputValue(value)

    if (value === "") {
      setDate(undefined)
      setError("")
      return
    }

    const parsedDate = parse(value, "MM/dd/yyyy", new Date())

    if (isValid(parsedDate) && value.length === 10) {
      setDate(parsedDate)
      setError("")
    } else {
      setDate(undefined)
      setError("Please enter a valid date in MM/DD/YYYY format")
    }
  }

  return (
    <Card className="w-full max-w-4xl mx-auto">
      <CardHeader>
        <CardTitle className="text-3xl font-bold text-center">The Year of the Snake</CardTitle>
        <p className="text-justify mt-1">
          The year of the snake, commencing on January 29, 2025, is characterized by wisdom, transformation, and adaptability. 
          Associated with intelligence and strategic thinking, this year encourages personal growth and 
          careful decision-making. The Wood element introduces flexibility and creativity, promoting 
          deeper reflection and thoughtful planning. Embracing change and long-term strategies will be 
          beneficial during this period. Overall, the Year of the Snake emphasizes introspection and 
          deliberate action.
        </p>
      </CardHeader>
      <CardContent>

        <Popover>
          <PopoverTrigger asChild>
            <Button
              variant={"outline"}
              className={cn("w-[280px] justify-start text-left font-normal", !date && "text-muted-foreground")}
            >
              <CalendarIcon className="mr-2 h-4 w-4" />
              {date ? format(date, "PPP") : <span>Pick a date</span>}
            </Button>
          </PopoverTrigger>
          <PopoverContent className="w-auto p-0" align="start">
            <div className="space-y-2 p-2">
              <div className="grid gap-2">
                <Input
                  type="text"
                  value={inputValue}
                  onChange={handleInputChange}
                  placeholder="MM/DD/YYYY"
                  className="w-[240px]"
                />
                {error && <p className="text-sm text-destructive">{error}</p>}
              </div>
              <Calendar mode="single" selected={date} onSelect={handleDateSelect} initialFocus />
            </div>
          </PopoverContent>
        </Popover>

        <Button
          onClick={async () => {
            if (date) {
              setLoading(true);
              try {
                const response = await fetch('http://localhost:8000/api/fengshui/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({ gregorian_birthday: format(date, "yyyy-MM-dd") }),
                });
                const data = await response.json();
                setFengShui(data.reading);
              } catch (error) {
                console.error('Error fetching zodiac data:', error);
              } finally {
                setLoading(false);
              }
            } else {
              setError("Please select a valid date before submitting");
            }
          }}
        >
          Read Feng Shui
        </Button>
        
        {loading && <p className="text-sm text-muted-foreground">Please wait while I'm reading your Feng Shui...</p>}
      
      </CardContent>
      {error && <p className="text-sm text-destructive">{error}</p>}

      {fengShui ? <FengShuiResults fengShui={fengShui} /> : ""}
    </Card>
  )
}
